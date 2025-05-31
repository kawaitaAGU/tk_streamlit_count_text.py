import streamlit as st

st.title("テキストファイル文字数カウンター")

uploaded_file = st.file_uploader("テキストファイルをアップロードしてください (.txt)", type=["txt"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")  # テキストを文字列として読み込み
    lines = content.splitlines()
    char_count_with_spaces = len(content)
    char_count_without_spaces = len(content.replace(" ", "").replace("\n", ""))
    word_count = len(content.split())

    st.subheader("解析結果")
    st.write(f"行数: {len(lines)}")
    st.write(f"文字数（空白含む）: {char_count_with_spaces}")
    st.write(f"文字数（空白除く）: {char_count_without_spaces}")
    st.write(f"単語数: {word_count}")

    with st.expander("テキスト全体を見る"):
        st.text_area("内容", value=content, height=300)
else:
    st.info("テキストファイル（.txt）をドラッグ＆ドロップ、または選択してください。")