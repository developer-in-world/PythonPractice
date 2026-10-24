class Movie:
    def __init__(self, movie_name: str, 
                 total_seats: int, 
                 ticket_price: int) -> None:
        
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0
    
    def show_status(self) -> None:
        print(f"Movie name: {self.movie_name}")
        print(f"Seats available for this movie: {self.total_seats}")
        print(f"Seats booked for this movie: {self.booked_seats}")
        
    def book_ticket(self, num_tickets: int) -> None:
        if num_tickets > self.total_seats - self.booked_seats:
            print("Sorry, not enough seats available")
        else:
            self.booked_seats += num_tickets
            self.total_seats -= num_tickets
            print(f"Your ticket is booked, kindly pay the amount: {self.ticket_price * num_tickets} to confirm the booking")


m1 = Movie("Wanda Vision", 300, 250)
m1.book_ticket(20)
m1.show_status()
m1.book_ticket(300)        