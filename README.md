# 简历优化 Agent

可运行的简历优化 Agent 应用。用户可输入/上传简历和目标 JD，系统先分析匹配度，再在用户确认后生成优化版简历并导出。

## 功能说明

1. 输入或上传简历内容（`.txt` / `.md`）
2. 输入目标岗位 JD
3. 一键输出：
   - 匹配亮点
   - 主要缺口
   - 具体优化建议
4. 用户勾选确认后生成优化版简历
5. 支持在页面查看并导出优化结果（`.md`）

## 环境变量配置

在项目根目录创建 `.env`（可复制 `.env.example`）：

```bash
cp .env.example .env
```

最少需要：

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



## 本地启动

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DEEPSEEK_API_KEY="your_api_key"
streamlit run app/streamlit_app.py
```

浏览器访问：`http://localhost:8501`

## Docker 构建与启动

### 1) 构建镜像

```bash
docker build -t resume-optimizer-agent .
```

### 2) 运行容器

```bash
docker run --rm -p 8501:8501 --env-file .env resume-optimizer-agent
```

浏览器访问：`http://localhost:8501`

## 使用流程

1. 上传或粘贴简历内容
2. 粘贴目标 JD
3. 点击「分析简历与JD匹配情况」
4. 查看分析结果并勾选确认
5. 点击「生成优化后简历」
6. 点击「导出优化简历（.md）」

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
tests/
```
