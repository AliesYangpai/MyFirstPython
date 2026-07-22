"""
PostToolUse Hook示例
监昕Write和Bash(rm)工具执行，记录文件操作日志
"""
import sys
import json
from pathlib import Path
from datetime import datetime

# 从stdin读取工具执行信息
try:
    input_data = json.loads(sys.stdin.read())
except:
    sys.exit(0)

# 获取工具名称和输入参数
tool_name = input_data.get('tool_name', '')
tool_input = input_data.get('tool_input', {})

# 记录日志（日志文件保存在当前项目目录下）
log_file = Path.cwd() / '.claude' / 'hooks' / 'log' / 'post-write.log'
log_file.parent.mkdir(parents=True, exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if tool_name == 'Write':
    file_path = tool_input.get('file_path', '')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] ✅ 文件写入: {file_path}\n")

elif tool_name == 'Bash':
    command = tool_input.get('command', '')
    # 匹配删除操作: rm, rm -rf, trash, unlink 等
    if any(cmd in command for cmd in ['rm ', 'rm -', 'trash ', 'unlink ']):
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] 🗑️ 文件删除: {command}\n")

elif tool_name == 'Edit':
    file_path = tool_input.get('file_path', '')
    new_string = tool_input.get('new_string', '')
    old_string = tool_input.get('old_string', '')
    # 如果新内容为空，视为删除操作
    if not new_string and old_string:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] ✏️ 内容删除: {file_path}\n")
    else:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] ✏️ 文件编辑: {file_path}\n")

sys.exit(0)
