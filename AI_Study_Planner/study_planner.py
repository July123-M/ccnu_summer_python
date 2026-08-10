"""
AI 学习计划生成器 - 大学生作业项目
功能：根据你输入的科目、时间和精力偏好，智能生成每日学习时间表
作者：AI 辅助编程
"""

import random
from datetime import datetime, timedelta

class AIStudyPlanner:
    """
    模拟AI决策引擎：根据人类认知规律，自动编排学习任务
    """
    
    def __init__(self):
        # 内置的AI知识库：不同学科推荐的学习时长（分钟）
        self.subject_duration_map = {
            "数学": 90,
            "英语": 60,
            "编程": 90,
            "物理": 80,
            "化学": 80,
            "政治": 50,
            "历史": 50,
            "语文": 60,
            "专业课": 90,
            "其他": 60
        }
        # 黄金学习时段（高效时间）
        self.golden_hours = [(8, 11), (15, 17), (19, 21)]
    
    def generate_plan(self, subjects_input, total_hours, intensity="适中"):
        """
        AI核心生成逻辑
        :param subjects_input: 用户输入的科目，逗号分隔，如 "数学,英语,编程"
        :param total_hours: 今天打算学习多少小时
        :param intensity: 学习强度（"轻松" / "适中" / "密集"）
        :return: 格式化的学习计划文本
        """
        # 1. 解析用户输入
        subject_list = [s.strip() for s in subjects_input.split(",") if s.strip()]
        
        if not subject_list:
            return "❌ AI检测到输入错误：请至少输入一个科目（用逗号隔开）。"
        
        # 2. AI算法：根据强度调整总时长和休息比例
        intensity_config = {
            "轻松": {"work_min": 45, "break_min": 15, "sessions": 1.0},
            "适中": {"work_min": 50, "break_min": 10, "sessions": 1.2},
            "密集": {"work_min": 55, "break_min": 5,  "sessions": 1.4}
        }
        config = intensity_config.get(intensity, intensity_config["适中"])
        
        # 计算总学习分钟数
        total_minutes = int(total_hours * 60)
        
        # AI决策：判断是否需要拆分过多科目（如果科目太多，缩短单科时长）
        avg_minutes = min(120, total_minutes // len(subject_list))
        
        # 3. 生成时间槽（AI排课逻辑）
        schedule = []
        current_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
        
        # 随机打乱科目顺序，避免总是先学同一个（模拟AI的随机优化）
        random.shuffle(subject_list)
        
        for subject in subject_list:
            # 从知识库获取推荐时长，否则取平均值
            default_duration = self.subject_duration_map.get(subject, 60)
            # 动态调整：如果科目列表很长，缩短单科时间以防止疲劳
            duration = min(default_duration, avg_minutes * 1.2)
            duration = max(30, duration)  # 最少学30分钟
            
            # 确保不超过剩余时间
            remaining = total_minutes - sum([d for _, d, _ in schedule])
            if remaining <= 0:
                break
            duration = min(duration, remaining)
            
            # AI判断：如果这个时间段在"黄金学习时段"，分配较难科目
            hour = current_time.hour
            is_golden = any(start <= hour < end for start, end in self.golden_hours)
            
            # 格式化时间显示
            start_str = current_time.strftime("%H:%M")
            end_time = current_time + timedelta(minutes=int(duration))
            end_str = end_time.strftime("%H:%M")
            
            # 添加一条计划
            schedule.append((subject, int(duration), start_str, end_str, is_golden))
            
            # 移动到下一个时间点
            current_time = end_time
            
            # AI决策：插入休息时间（根据强度配置）
            if len(schedule) < len(subject_list):
                break_minutes = config["break_min"]
                current_time += timedelta(minutes=break_minutes)
        
        # 4. 格式化输出漂亮的计划表
        return self._format_output(schedule, intensity)
    
    def _format_output(self, schedule, intensity):
        """AI输出美化器：生成美观的文字表格"""
        if not schedule:
            return "⚠️ AI无法生成有效计划，请检查输入参数。"
        
        lines = []
        lines.append("=" * 50)
        lines.append("🤖 AI 智能学习计划生成报告")
        lines.append(f"📊 学习强度：{intensity} | 总科目数：{len(schedule)}")
        lines.append("=" * 50)
        lines.append("")
        lines.append("┌──────────┬─────────────┬──────────────┬──────────┐")
        lines.append("│  🕐 时间  │   📚 科目   │   ⏱️ 时长   │  🧠 状态 │")
        lines.append("├──────────┼─────────────┼──────────────┼──────────┤")
        
        for subject, duration, start, end, is_golden in schedule:
            # 根据是否黄金时间标记状态
            status = "⭐ 高效" if is_golden else " 一般  "
            time_slot = f"{start}-{end}"
            duration_str = f"{duration}分钟"
            # 中文对齐占位（简单处理）
            subject_display = subject.ljust(11)
            lines.append(f"│ {time_slot} │ {subject_display}│ {duration_str:^10} │ {status}  │")
        
        lines.append("└──────────┴─────────────┴──────────────┴──────────┘")
        lines.append("")
        lines.append("💡 AI学习建议：")
        lines.append("   1. ⭐ 标记为'高效'的时段，建议攻克最难科目。")
        lines.append("   2. ☕ 每学习50分钟，起身活动5-10分钟。")
        lines.append("   3. 📈 持续优化：根据今天执行情况，明天调整输入参数。")
        lines.append("=" * 50)
        return "\n".join(lines)

# ------------------ 程序入口（用户交互界面）------------------
if __name__ == "__main__":
    print("\n🎓 欢迎使用 AI 学习计划生成器 （大学生作业版）")
    print("提示：本程序模拟AI决策算法，根据认知科学自动排课。\n")
    
    # 用户输入（带异常处理）
    try:
        subjects = input("📝 请输入今天要学的科目（用英文逗号隔开，如：数学,英语,编程）: ")
        hours = float(input("⏰ 请输入今天计划学习总时长（小时，如 3 或 4.5）: "))
        intensity = input("💪 请选择学习强度（轻松 / 适中 / 密集）: ")
        
        if intensity not in ["轻松", "适中", "密集"]:
            print("⚠️ 输入错误，默认使用 '适中' 强度。")
            intensity = "适中"
        
        # 调用AI生成器
        planner = AIStudyPlanner()
        result = planner.generate_plan(subjects, hours, intensity)
        
        print("\n" + result)
        
    except ValueError:
        print("❌ 输入错误：总时长请输入数字（如 3 或 4.5）。")
    except Exception as e:
        print(f"❌ 程序运行异常：{e}")
    
    input("\n按 Enter 键退出...")