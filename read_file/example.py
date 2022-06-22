def use_while():
    msg = ''
    with open("story") as f:
        while True:
            txt = f.read(10)
            if not txt:
                break
            msg += txt
    print(msg)


def use_for():
    msg = ''
    with open("story") as f:
        for txt in f.read(10):
            msg += txt
    print(msg)


if __name__ == '__main__':
    use_for()
    print("="*70)
    use_while()