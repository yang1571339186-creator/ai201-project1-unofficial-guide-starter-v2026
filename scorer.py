def judge(question, expects,answer,  results) -> bool:
    expected_chunk = expects.split(" ")
    for piece in expected_chunk:
        if piece not in answer:
            return False
    return True
