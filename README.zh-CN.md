# CWU7 - 7 点起床困难户

一个模块化的 Python 自动化工具包，包含多个独立工具，用于各种自动化和开发任务。该工具包采用平等状态的工具设计，可以单独使用或组合使用，并具有易于扩展新自动化工具的能力。

## 🚀 工具包概览

CWU7 由多个独立工具组成，每个工具都有特定的自动化用途：

### 🏸 羽毛球场预约工具 ([`court_reservation.py`](tools/court_reservation.py))

具有智能计时和错误处理的自动化羽毛球场预约系统：

- **⏰ 精确计时**：等到早上 7:00 准时开始预约流程
- **🤖 自动导航**：自动点击预约界面的各个步骤
- **🔍 验证码识别**：使用 OCR 技术识别并解决验证码挑战
- **🔄 重试机制**：失败时自动重试，可配置重试次数
- **📝 完整日志**：将所有操作和错误记录到文件和控制台

### 🎯 鼠标位置跟踪器 ([`mouse_tracker.py`](tools/mouse_tracker.py))

用于 UI 自动化坐标发现的开发工具：

- **📍 实时坐标**：显示实时鼠标位置和像素颜色信息
- **🖱️ 开发友好**：对于确定自动化脚本的点击坐标至关重要
- **⚡ 低延迟**：可配置刷新率以获得最佳性能
- **🎨 颜色检测**：显示 RGB 值以进行精确的基于颜色的自动化

### 💬 Copilot 会话恢复工具 ([`copilot_resumption.py`](tools/copilot_resumption.py))

用于自动化开发辅助的智能会话管理工具：

- **👁️ 屏幕监控**：监控特定屏幕区域的颜色变化
- **🤖 自动响应**：在需要交互时自动输入文本
- **🔄 会话连续性**：帮助在无需手动干预的情况下保持活跃的 Copilot 会话
- **📊 活动日志**：跟踪所有监控和响应活动

## 系统要求

- Python 3.6+
- Windows 操作系统
- 所需 Python 包：
  - pyautogui
  - ddddocr
  - numpy
  - Pillow

## 安装说明

```shell
# 克隆仓库
git clone https://github.com/xixu-me/CWU7.git
cd CWU7

# 安装依赖
pip install pyautogui ddddocr numpy Pillow
```

## 📖 工具使用方法

CWU7 工具包中的每个工具都可以独立使用。选择适合您当前自动化需求的工具：

### 🏸 羽毛球场预约工具

在精确时间自动化羽毛球场预约：

1. 如需要，在 `court_reservation.py` 中配置预约设置
2. 运行工具：

   ```shell
   python tools/court_reservation.py
   ```

工具将等到配置的时间并自动处理整个预约流程。

### 🎯 鼠标位置跟踪器

为自动化脚本发现 UI 坐标：

```shell
python tools/mouse_tracker.py
```

跟踪器显示实时鼠标位置和像素颜色信息。当您找到所需坐标时，按 Ctrl+C 退出。

### 💬 Copilot 会话恢复工具

自动维护活跃的 Copilot 会话：

```shell
python tools/copilot_resumption.py
```

该工具监控屏幕区域并自动响应交互提示以保持 Copilot 会话活跃。

## ⚙️ 工具配置

每个工具都有自己的配置选项。请参考其源文件内的特定工具文档：

### 羽毛球场预约工具

- **时间设置**：在 `court_reservation.py` 中修改 `RESERVATION_HOUR` 和 `RESERVATION_MINUTE`
- **UI 坐标**：使用跟踪器工具找到的坐标更新 `COORDINATES` 字典
- **重试设置**：配置 `MAX_RETRY_ATTEMPTS` 进行错误处理

### 鼠标位置跟踪器

- **刷新率**：修改 `refresh_rate` 参数以调整更新频率
- **显示格式**：在跟踪器函数中自定义输出格式

### Copilot 会话恢复工具

- **监控区域**：设置颜色监控的屏幕坐标
- **目标颜色**：配置用于检测交互需求的 RGB 值
- **响应文本**：自定义自动输入文本

## 🔧 工作原理

工具包为每个工具采用不同的自动化策略：

### 羽毛球场预约工作流程

1. 等待目标时间
2. 打开预约界面
3. 自动完成预约步骤
4. 识别并处理验证码
5. 失败自动重试
6. 记录所有操作和结果

### 鼠标跟踪器操作

1. 持续捕获鼠标位置
2. 读取光标位置的像素颜色
3. 显示格式化的坐标和颜色数据
4. 以可配置的间隔更新

### Copilot 恢复流程

1. 监控指定的屏幕区域
2. 检测表明交互需求的颜色变化
3. 自动输入配置的响应文本
4. 记录所有监控活动

## 🔧 故障排除

### 通用问题

- **Python 依赖**：确保通过 pip 安装所有必需的包
- **屏幕分辨率**：根据您的特定显示配置更新坐标
- **权限问题**：如果自动化被阻止，请以适当的权限运行

### 特定工具问题

#### 羽毛球场预约工具

- **坐标错误**：使用 `mouse_tracker.py` 找到正确的 UI 元素位置
- **验证码失败**：OCR 可能需要针对不同验证码样式进行调整
- **时序问题**：在工具配置中调整 `check_interval`

#### 鼠标位置跟踪器

- **高 CPU 使用率**：增加刷新率间隔以降低资源消耗
- **坐标精度**：确保在测量中考虑显示缩放

#### Copilot 会话恢复工具

- **颜色检测**：验证 RGB 值与实际屏幕颜色匹配
- **响应时间**：调整监控间隔以获得更好的响应性

详细日志请检查相应的日志文件：`reservation.log` 和 `copilot_resumption.log`。

## 🚀 扩展工具包

CWU7 设计为易于扩展。要添加新的自动化工具：

### 添加新工具

1. **创建工具文件**：将新工具添加到 `tools/` 目录
2. **遵循结构**：使用现有工具作为日志和配置的模板
3. **更新文档**：在两个 README 文件中添加工具描述
4. **测试集成**：确保工具能独立工作并与其他工具协同

### 开发指南

- **模块化设计**：每个工具应该是自包含的并可独立执行
- **一致的日志**：使用已建立的日志格式以保持一致性
- **配置**：使设置易于配置以适应不同用例
- **错误处理**：实现健壮的错误处理和重试机制

## ⚖️ 法律声明

本软件仅供教育目的。用户有责任遵守他们交互的任何系统的服务条款。作者不对误用或使用本工具包的任何后果负责。

## 📄 许可证

GNU 通用公共许可证 v3.0 - 详见 [LICENSE](LICENSE) 文件。

## 🤝 贡献

我们欢迎为扩展 CWU7 工具包做出贡献：

1. Fork 仓库
2. 创建功能分支 (`git checkout -b feature/new-tool`)
3. 提交带有清晰消息的更改
4. 推送到您的分支 (`git push origin feature/new-tool`)
5. 创建带有详细描述的 Pull Request

### 贡献指南

- 遵循现有的代码风格和结构
- 为新工具添加全面的文档
- 包含错误处理和日志记录
- 在 Windows 环境中充分测试
- 更新英文和中文 README 文件

## ⚠️ 免责声明

此工具包仅设计用于合法的自动化目的。用户必须：

- 尊重目标系统的服务条款
- 负责任和道德地使用工具
- 遵守适用的法律法规
- 对其使用承担全部责任

作者对误用或因使用此工具包而产生的任何后果不承担任何责任。
