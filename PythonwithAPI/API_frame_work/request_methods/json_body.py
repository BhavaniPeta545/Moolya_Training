import random

authentication= "/api-clients/"
order_resource="/orders/"
num=str(random.randint(100,200))
booknum=str(random.randint(1,5))
auth={
    "clientName": "Postman" +num+ "nae",
    "clientEmail": "valentin"+num+"@example.com"
}
submit_book={
    "bookId": booknum,
    "customerName": "bhavani"+num
}
update_book={
  "customerName": "John5"
}