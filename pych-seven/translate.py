def trans(x):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','5','8','13','21','34','55','89','144','233','377','610','987','1597',
           '2584','4181','6765','10946','17711','28657','46368','75025','121393','196418']
    translate_code = {}
    for alphabet,number in zip(alphabets,numbers):
        translate_code[number] = alphabet

    return translate_code['%d'%x]
