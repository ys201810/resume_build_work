# coding=utf-8
import os
import gradio as gr
import openai
import pathlib
from resume_build_utils import make_prompt
from prompts import generate_resume, generate_advice, brushup_resume_normal, brushup_resume_byformat
from dotenv import load_dotenv

base_path = pathlib.Path.cwd().parent
prompt_path = base_path / 'prompt'
load_dotenv(verbose=True)
load_dotenv(base_path / 'env_file' / '.env')

openai.api_key = os.environ.get("API_KEY")
model = os.environ.get("USE_MODEL")


def generate_and_brushup_resume(job_title: str, position: str, mission: str, domain: str):
    # 1. 入力の4つのテキストから職務経歴のテキストを生成する。
    prompt_file = prompt_path / 'resume_make.txt'
    prompt_params = {
        'job_title': job_title,
        'position': position,
        'mission': mission,
        'domain': domain
    }
    resume = generate_resume(prompt_file, prompt_params, openai, model)

    # 2. 職務経歴のテキストにアドバイスをもらう。
    prompt_file = prompt_path / 'resume_advice.txt'
    prompt_params = {
        'text': resume,
    }
    advice_text = generate_advice(prompt_file, prompt_params, openai, model)

    # 3. 職務経歴のテキストとアドバイスで職務経歴のテキストを魅力的にする(フリーフォーマット)。
    prompt_file = prompt_path / 'resume_brushup_normal.txt'
    prompt_params = {
        'org_resume': resume,
        'advice_text': advice_text
    }
    brushuped_resume = brushup_resume_normal(prompt_file, prompt_params, openai, model)

    # 4. 職務経歴のテキストとアドバイスで職務経歴のテキストを魅力的にする(フォーマット指定)。
    prompt_file = prompt_path / 'resume_brushup_formatted.txt'
    prompt_params = {
        'org_resume': resume,
        'advice_text': advice_text
    }
    formatted_resume = brushup_resume_byformat(prompt_file, prompt_params, openai, model)

    return resume, advice_text, brushuped_resume, formatted_resume


def run():
    # 入力設定
    inputs = [
        gr.inputs.Textbox(label="職種"),
        gr.inputs.Textbox(label="ポジション"),
        gr.inputs.Textbox(label="ミッション"),
        gr.inputs.Textbox(label="担当領域"),
    ]

    # 出力設定
    outputs = [
        gr.outputs.Textbox(label="生成された職務経歴"),
        gr.outputs.Textbox(label="より魅力的にするためのアドバイス"),
        gr.outputs.Textbox(label="自動的にブラッシュアップした職務経歴"),
        gr.outputs.Textbox(label="フォーマットに沿った職務経歴"),
    ]

    # 説明文設定
    title = "職務経歴書生成デモ"
    description = "職種、ポジション、ミッション、担当領域のテキストと強調したいテキストを入力して、職務経歴書を生成し、魅力的に強調します。"
    article = """
    職種：　営業/販売サービス/ITエンジニア/事務アシスタントなどの仕事の種類を入力します。\n
    ポジション：　グループマネージャー、チームマネージャー、メンバー、メンターなどの役割を入力します。\n
    ミッション：　仕事の目的を記載します。\n
    担当領域：　仕事の中でご自身が担当した範囲や担った役割を記載します。
    """

    # 実行
    iface = gr.Interface(
        fn=generate_and_brushup_resume,
        inputs=inputs,
        outputs=outputs,
        title=title,
        description=description,
        article=article
    )
    iface.launch()


if __name__ == '__main__':
    run()