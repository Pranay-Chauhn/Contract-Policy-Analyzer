from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_to_chunks(text, chunk_size=5000, chunk_overlap=300):
    spliter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return spliter.split_text(text)
