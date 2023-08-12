# coding=utf-8
def make_prompt(prompt_file: str, prompt_params: dict) -> str:
    """
    GPTに投入するプロンプトを作成する。promptファイルパスと、そこに埋め込むテキストの辞書が入力。
    :param prompt_file: プロンプトファイルのパス。
    :param prompt_params: プロンプト内で置換する文章の辞書。
    :return: プロンプトの文章
    """
    with open(prompt_file, 'r') as inf:
        prompt = inf.read()
    return prompt.format(**prompt_params)
