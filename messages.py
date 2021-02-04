def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
    print(messages, '\n', sent_messages)

testListMessages = ['Hellow', 'Bazinga', 'Aliens', 'Python']
testSentMessages = []
show_messages(testListMessages)
send_messages(testListMessages[:], testSentMessages)
print(testListMessages)
