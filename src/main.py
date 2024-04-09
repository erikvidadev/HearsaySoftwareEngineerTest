from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI()


def sort_data(payload: Dict[str, List[str]], sort_keys: List[str]) -> Dict[str, List[str]]:
    try:
        for key in sort_keys:
            if key in payload:
                payload[key] = sorted(payload[key])
        return payload
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/sort")
async def sort_json(data: Dict[str, Dict[str, List[str]]]) -> Dict[str, List[str]]:
    return sort_data(data.get('data', {}), data.get('sortKeys', {}).get('keys', []))


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5000)
