from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AnalyzeRequest(BaseModel):
    url: str
    preferred_language: str = "zh"
    depth: str = "deep"
    user_goal: Optional[str] = None


@app.get("/")
def home():
    return {
        "ok": True,
        "message": "Backend is running."
    }


@app.post("/youtube/analyze")
def analyze_youtube_video(payload: AnalyzeRequest):
    return {
        "video": {
            "video_id": "demo123",
            "url": payload.url,
            "title": "Demo video",
            "channel": "Demo channel",
            "published_at": "2026-04-07T00:00:00Z",
            "duration_sec": 600
        },
        "transcript": {
            "available": False,
            "source_type": "none",
            "language": payload.preferred_language,
            "coverage_ratio": 0,
            "segments": []
        },
        "chapters": [],
        "teaching_payload": {
            "one_minute_brief": "当前仅完成接口联调，尚未接入真实 YouTube 解析。",
            "structure": [
                "这是一个最小可运行后端",
                "下一步会接入真实视频解析"
            ],
            "key_concepts": [
                {
                    "name": "Action backend",
                    "explanation": "让 GPT 通过外部 API 获取结构化数据"
                }
            ],
            "core_claims": [
                "现在已经可以打通 GPT 调用你自己的 API 这条链"
            ],
            "likely_misconceptions": [
                "这个版本还不会真正理解 YouTube 视频"
            ],
            "internalization_prompts": [
                "先验证 API 能被 GPT 成功调用",
                "再接真实的视频元数据和字幕逻辑"
            ]
        },
        "limitations": [
            "No transcript pipeline connected yet."
        ]
    }
