# 简历优化 Agent

可运行的简历优化 Agent 应用。用户可输入或上传简历、输入目标岗位 JD，系统先分析匹配度，再在用户确认后生成优化后的简历内容并支持导出。

## 功能说明

1. 输入或上传简历内容（`.txt` / `.md`）
2. 输入目标岗位 JD
3. 自动分析简历与 JD 的匹配情况，并输出：
   - 匹配亮点
   - 主要缺口
   - 具体优化建议
4. 用户确认后生成优化后的完整简历
5. 支持在页面查看并导出优化结果（`.md`）

## 环境变量配置

在项目根目录创建 `.env` 文件，可直接复制 `.env.example`：

```bash
cp .env.example .env
```

最少需要以下环境变量：

```env
DEEPSEEK_API_KEY=your_api_key
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat
```

阿里云百炼（OpenAI 兼容）示例：

```env
DEEPSEEK_API_KEY=sk-xxxx
DEEPSEEK_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DEEPSEEK_MODEL=deepseek-v3.2
```

说明：

- API Key 仅通过环境变量读取，不会硬编码在代码中
- 应用会自动读取项目根目录中的 `.env`
- 浏览器访问请使用 `127.0.0.1`
- 部分运行日志中会显示 `0.0.0.0:8501`，该地址为服务监听地址

## 本地启动

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env，填入真实 DEEPSEEK_API_KEY
./run.sh
```

浏览器访问：`http://127.0.0.1:8501`

如果 `run.sh` 没有执行权限，可使用：

```bash
bash run.sh
```

如果端口 `8501` 已被占用，可使用：

```bash
PORT=8502 ./run.sh
```

然后访问：`http://127.0.0.1:8502`

## Docker 构建与启动

### 1) 构建镜像

```bash
docker build -t resume-optimizer-agent .
```

### 2) 运行容器

```bash
docker run --rm -p 8501:8501 --env-file .env resume-optimizer-agent
```

浏览器访问：`http://127.0.0.1:8501`

如果端口 `8501` 已被占用，可改用：

```bash
docker run --rm -p 8502:8501 --env-file .env resume-optimizer-agent
```

然后访问：`http://127.0.0.1:8502`

## 面试官快速验收

仅需以下步骤即可启动并完成基本验收：

```bash
git clone https://github.com/hkcmi/resume_agent.git
cd resume_agent
cp .env.example .env
# 编辑 .env，填入真实 DEEPSEEK_API_KEY
docker build -t resume-optimizer-agent .
docker run --rm -p 8501:8501 --env-file .env resume-optimizer-agent
```

打开 `http://127.0.0.1:8501` 后：

1. 上传或粘贴简历内容
2. 粘贴目标岗位 JD
3. 点击「分析简历与JD匹配情况」
4. 查看分析结果并勾选确认
5. 点击「生成优化后简历」
6. 点击「导出优化简历（.md）」

## 使用流程

1. 上传或粘贴简历内容
2. 粘贴目标岗位 JD
3. 点击「分析简历与JD匹配情况」
4. 查看系统输出的匹配亮点、主要缺口、具体优化建议
5. 勾选确认后点击「生成优化后简历」
6. 在页面查看优化结果并下载 `.md` 文件

## 实现说明

- Web 框架：Streamlit
- LLM 服务：DeepSeek OpenAI 兼容接口
- 两阶段流程：
  - 第一步：分析简历与 JD 的匹配度
  - 第二步：用户确认后生成优化后的完整简历
- 提示词约束：
  - 分析阶段固定输出结构化结果
  - 优化阶段要求不伪造未提供的经历与事实

## 项目结构

```text
app/
  streamlit_app.py      # Web 应用入口
  llm_client.py         # DeepSeek API 调用
  resume_optimizer.py   # 分析与优化提示词构建
  tools.py              # 文本处理和结果分段辅助函数
Dockerfile
requirements.txt
.env.example
run.sh
tests/
```
