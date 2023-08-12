# coding=utf-8
import openai

from resume_build_utils import make_prompt

def generate_resume(prompt_file: str, prompt_params: dict, openai: openai, model: str) -> str:
    # プロンプトの作成
    prompt = make_prompt(prompt_file, prompt_params)

    # レスポンスの取得
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
    )
    return response['choices'][0]['message']['content'].strip()

def generate_advice(prompt_file: str, prompt_params: dict, openai: openai, model: str) -> str:
    # プロンプトの作成
    prompt = make_prompt(prompt_file, prompt_params)

    # レスポンスの取得
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
    )
    return response['choices'][0]['message']['content'].strip()

def brushup_resume_normal(prompt_file: str, prompt_params: dict, openai: openai, model: str) -> str:
    # プロンプトの作成
    prompt = make_prompt(prompt_file, prompt_params)

    # レスポンスの取得
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
    )
    return response['choices'][0]['message']['content'].strip()

def brushup_resume_byformat(prompt_file: str, prompt_params: dict, openai: openai, model: str) -> str:
    # プロンプトの作成
    prompt = make_prompt(prompt_file, prompt_params)

    # レスポンスの取得
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
    )
    return response['choices'][0]['message']['content'].strip()
