import time
import winsound
import sys

def focus_timer(duration, break_duration):
    print(f"专注开始，持续 {duration} 分钟...")
    time.sleep(duration * 60)  # 将分钟转换为秒
    winsound.Beep(1000, 1000)  # 响一声，提醒专注结束

    print(f"休息开始，持续 {break_duration} 分钟...")
    time.sleep(break_duration * 60)  # 将分钟转换为秒
    winsound.Beep(1000, 1000)  # 响一声，提醒休息结束

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python focus_timer.py <专注时间（分钟）> <休息时间（分钟）>")
        sys.exit(1)
    
    try:
        focus_time = int(sys.argv[1])
        break_time = int(sys.argv[2])
        
        while True:
            focus_timer(focus_time, break_time)
    except ValueError:
        print("Invalid input. Please provide valid integer values for focus and break time.")
