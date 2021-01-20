ticket_num = int(input("Введите количество билетов "));
tickets_price = 0;
for i in range(ticket_num):
    temp = int(input("Введите возраст зртеля "));
    if temp >= 18:
        if temp < 25:
            tickets_price = tickets_price + 990;
        else:
            tickets_price = tickets_price + 1390;

if(ticket_num > 3):
    tickets_price = tickets_price * 0.9;
print(tickets_price);
