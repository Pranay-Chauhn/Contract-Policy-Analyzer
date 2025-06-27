from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_to_chunks(text, chunk_size=1000, chunk_overlap=100):
    spliter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return spliter.create_document([text])
