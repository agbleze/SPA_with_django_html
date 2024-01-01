
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
import time
import threading
from random import randint
from channels.generic.websocket import JsonWebsocketConsumer
from django.template.loader import render_to_string


class EchoConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        
        self.send(text_data="You are connected by WebSocket!")
        
        def send_time(self):
            
            while True:
                self.send(text_data=str(datetime.now().strftime("%H:%M:%S")))
                time.sleep(1)
                
        threading.Thread(target=send_time, args=(self, )).start()
        
    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        pass
    

class BingoConsumer(JsonWebsocketConsumer):
    
    def connect(self):
        self.accept()
        
        random_numbers = list(set([randint(1, 10) for _ in range(5)]))
        
        message = {
            'action': 'New ticket',
            'ticket': random_numbers
        }
        
        self.send_json(content=message)
        
        def send_ball(self):
            while True:
                random_ball = randint(1, 10)
                message = {
                    'action': 'New ball',
                    'ball': random_ball
                }
                self.send_json(content=message)
                time.sleep(1)
                
        threading.Thread(target=send_ball, args=(self,)).start()
            
    def disconnect(self, close_code):
        pass
    
    def receive_json(self, data):
        pass
    
class BMIConsumer(JsonWebsocketConsumer):
    
    def connect(self):
        self.accept()
        
    def disconnect(self, close_code):
        pass
    
    def receive_json(self, data):
        height = data['height'] / 100
        weight = data['weight']
        bmi = round(weight / (height ** 2), 1)
        self.send_json(
            content={
                "action": "BMI result",
                "html": render_to_string(template_name="components/_bmi_result.html", 
                                         context={"height": height, "weight": weight, "bmi": bmi}
                                         )
            }
        )

        



