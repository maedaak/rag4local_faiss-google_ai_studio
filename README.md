# ローカルマシンのFAISSとGoogle AI StudioのAPIでRAG

## mk-faiss_vectorstore.py
- 指定のディレクトリにあるテキスト(Markdownt等）をもとにFAISS(ベクトルストア）をデータファイルを作成する
- 稼働確認をした環境はWindows11マシン(GPUあり）のWSL(Ubuntu)

## simple_rag.py
- FAISSのデータファイルとGoogle AI StudioのAPIを使い、簡単なRAGを実現する
- 実行には**環境変数にGoogle AI Studioを設定**する必要がある
- 実行するとプロンプト入力（ただし1行のみ）が表示されるので、ここで質問をする
- 結果はディスプレイに表示するだけではなく、answer_実行日時分秒.mdのMarkdownでも出力する
- Google AI Studioの無料APIを使っているので、**機密性のある情報のやりとりはしないように**注意のこと
