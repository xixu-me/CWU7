# CWU7 - 7点起床困难户

一个用于在早上7点准时预约羽毛球场的Python自动化工具。

## 概述

CWU7 可以自动在配置的时间（默认7:00 AM）准时预约羽毛球场。如果你讨厌早起抢场地，这个工具可以帮你：

- 自动导航预约网站
- 使用OCR技术处理验证码
- 精确计时预约操作
- 记录整个过程

## 功能

- **精确计时**: 在配置的时间（默认7:00 AM）准时执行
- **验证码识别**: 使用OCR技术自动识别验证码
- **坐标追踪**: 包含获取UI元素坐标的工具
- **详细日志**: 记录预约全过程方便排查问题

## 安装

1. 克隆仓库:

   ```bash
   git clone https://github.com/yourusername/CWU7.git
   cd CWU7
   ```

2. 安装依赖:

   ```bash
   pip install pyautogui pillow numpy ddddocr
   ```

## 使用

### 鼠标坐标追踪器

使用预约机器人前，需要先确定各UI元素的屏幕坐标:

```bash
python tracker.py
```

将鼠标移动到重要UI元素上并记录坐标，然后在run.py文件中更新这些坐标。

### 预约机器人

运行预约机器人:

```bash
python run.py
```

默认情况下，机器人会等到早上7:00开始预约流程。

## 配置

编辑run.py中的以下常量来自定义机器人:

- `RESERVATION_HOUR` 和 `RESERVATION_MINUTE`: 设置预约的目标时间
- `COORDINATES`: 调整各UI元素的屏幕坐标
- `WAIT_TIMES`: 根据需要修改操作之间的等待时间

```python
# 配置示例
RESERVATION_HOUR = 7  # 目标小时(24小时制)
RESERVATION_MINUTE = 0  # 目标分钟
COORDINATES = {
    "badminton_button": (1101, 223),
    # ...其他坐标
}
```

## 工作原理

1. 脚本等待到配置的时间（默认7:00 AM）
2. 执行一系列点击操作导航预约界面
3. 如果出现验证码:
   - 从屏幕捕获验证码图像
   - 使用OCR识别文本
   - 输入识别出的文本
   - 提交表单
4. 整个过程会记录到控制台和文件(`reservation.log`)

## 故障排除

- 如果机器人点击位置不对，使用tracker.py验证并更新坐标
- 检查`reservation.log`获取详细错误信息
- 确保屏幕分辨率与配置坐标时使用的分辨率一致

## 免责声明

本工具仅用于教育目的。使用自动化机器人可能违反某些预约系统的服务条款。使用风险自负。

## 许可证

采用 [GPL-3.0](LICENSE) 许可证授权。
