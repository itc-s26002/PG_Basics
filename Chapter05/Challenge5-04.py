zisho = {
    "身長": "151",
    "好きな色": "緑",
    "好きなもの": "お菓子"
}

answer = input("身長,好きな色,好きなもの:")
if answer in zisho:
    result = zisho[answer]
    print(result)
