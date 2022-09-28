def fbtranslate(text):
    mname1="Helsinki-NLP/opus-mt-en-ru"
    #mname1="/content/drive/MyDrive/facebook/wmt19-en-ru"
    tokenizer2 = FSMTTokenizer.from_pretrained(mname1)
    model2 = FSMTForConditionalGeneration.from_pretrained(mname1)
    # # Saving the Models
    #tokenizer2.save_pretrained(mname1)
    #model2.save_pretrained(mname1)
    # input =decoded
    input_ids = tokenizer2.encode(text, return_tensors="pt")
    outputs = model2.generate(input_ids)
    decoded = tokenizer2.decode(outputs[0], skip_special_tokens=True)
    # print(decoded) # Машинное обучение - это здорово, не так ли?
    

    mname2="Helsinki-NLP/opus-mt-ru-en"  
    tokenizer2 = FSMTTokenizer.from_pretrained(mname2)
    model2 = FSMTForConditionalGeneration.from_pretrained(mname2)
    # # Saving the Models
    #tokenizer2.save_pretrained(mname2)
    #model2.save_pretrained(mname2)
    # input =decoded
    input_ids = tokenizer2.encode(decoded, return_tensors="pt")
    outputs = model2.generate(input_ids)
    decoded = tokenizer2.decode(outputs[0], skip_special_tokens=True)
    print(decoded) # Машинное обучение - это здорово, не так ли?

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    fullTranslatedText = [] 
    for para in doc.paragraphs:
      trans =fbtranslate(para.text)
      if trans == None :
        continue
      print(trans)
    print(fullText)
    print(fullTranslatedText)
    
