


class Car:
    def __init__(self):
        self.link=str()
        self.model=str()
        self.engine=str()
        self.price=float()
        self.installment=float()
        self.prod_year=int()
        self.vin=str()
        self.color=str()
        # self.photos=[]
    def car_info(self,inf):
        car_items_list=[self.link,self.model,self.engine,self.price,self.installment,self.prod_year,self.vin,self.color]
        for i in range(len(car_items_list)):
            inf[i].append(car_items_list[i])
        return inf