# CWU7 - 7 点起床困难户

一个用于在早上 7:00 准时预约羽毛球场地的 Python 自动化脚本。该工具集还包含 UI 坐标辅助工具和 Copilot 会话恢复工具。

## 功能特性

### 核心预约机器人

- **精确计时**：等到早上 7:00 准时开始预约流程
- **自动导航**：自动点击预约界面的各个步骤
- **验证码识别**：使用 OCR 技术识别并解决验证码挑战
- **重试机制**：失败时自动重试，可配置重试次数
- **完整日志**：将所有操作和错误记录到文件和控制台

### 辅助工具

- **鼠标跟踪工具**：用于查找 UI 坐标的辅助工具
- **Copilot 恢复工具**：自动化工具，用于在需要交互时恢复 Copilot 会话

## 系统要求

- Python 3.6+
- Windows 操作系统
- 所需 Python 包：
  - pyautogui
  - ddddocr
  - numpy
  - Pillow

## 安装说明

```powershell
# 克隆仓库
git clone https://github.com/xixu-me/CWU7.git
cd CWU7

# 安装依赖
pip install pyautogui ddddocr numpy Pillow
```

## 使用方法

### 运行预约机器人

1. 如需要，在 `court_reservation.py` 中配置预约时间和坐标
2. 运行主脚本：

   ```powershell
   python court_reservation.py
   ```

机器人将等到早上 7:00，然后自动尝试预约羽毛球场地。

### 鼠标位置跟踪器

查找 UI 元素的坐标：

```powershell
python tracker.py
```

实时显示当前鼠标位置和像素颜色。按 Ctrl+C 退出。

### Copilot 恢复工具

自动继续 Copilot 会话：

```powershell
python copilot_resumption.py
```

该工具监控特定屏幕区域的颜色变化，并在检测到目标颜色时自动输入文本，帮助在需要交互时恢复或继续 Copilot 会话。

## 配置说明

- **时间设置**：修改 `court_reservation.py` 中的 `RESERVATION_HOUR` 和 `RESERVATION_MINUTE`
- **坐标配置**：`court_reservation.py` 中的 `COORDINATES` 字典包含所有点击位置。用 `tracker.py` 获取正确坐标
- **重试设置**：`court_reservation.py` 中设置 `MAX_RETRY_ATTEMPTS`

## 工作原理

1. 等待目标时间
2. 打开预约界面
3. 自动完成预约步骤
4. 识别并处理验证码
5. 失败自动重试
6. 记录所有操作和结果

## 文件结构

- `court_reservation.py` - 主要预约机器人脚本
- `tracker.py` - 鼠标位置跟踪工具
- `copilot_resumption.py` - Copilot 会话恢复工具
- `captcha.png` - 验证码样例图片
- `LICENSE` - 许可证
- `.gitignore` - Git 忽略文件
- `reservation.log` - 预约日志（运行时生成）
- `copilot_resumption.log` - Copilot 工具日志（运行时生成）

## 故障排除

- **坐标错误**：用 `tracker.py` 查找正确点击位置
- **验证码失败**：OCR 可能需针对不同验证码样式调整
- **时序问题**：调整代码中的 `check_interval`
- **屏幕分辨率**：根据显示器调整坐标

日志：详见 `reservation.log` 和 `copilot_resumption.log`

## 法律声明

本软件仅供教育目的。用户有责任遵守预约系统的服务条款。作者不对任何误用或违规行为负责。

## 许可证

本项目采用 GNU 通用公共许可证 v3.0 - 详见 [LICENSE](LICENSE) 文件。

## 贡献

1. Fork 仓库
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 免责声明

这是一个旨在帮助合法预约的自动化工具。请负责任地使用，并遵守预约系统的服务条款。
