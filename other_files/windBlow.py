from pynput import keyboard
import threading
import time

a='a'
l=20

global range_
range_ = 21

class Bass(object):
    def __init__(self, change):
        self.change = change

    def windBlowL(self, lrange):
        for i in reversed(range(1,lrange)):
            print((a*i)+ ' ' + (((a*l)+' ')*3)+ (a*(l-i)))
            time.sleep(.1)
            if self.change == 'r':
                self.windBlowR(i)
                break

    def windBlowR(self, rrange):
        for i in reversed(range(1,rrange)):
            print((a*(l-i))+ ' ' + (((a*l)+' ')*3)+ (a*i))
            time.sleep(.1)
            if self.change == 'l':
                self.windBlowL(i)
                break

    def on_press(self, key):
        try:
            self.change = str(key.char)
            # print('Alphanumeric key pressed: {0} '.format(key.char))
        except AttributeError:
            print('special key pressed: {0}'.format(key))

    def on_release(self, key):
        # print('\n')
        # print('Key released: {0}'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def KeyboardListener(self):
        print("here")
        # on_press_func = lambda change: on_press(key, change)
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def windBlow(self):
        self.windBlowL(range_) if self.change == 'l' else self.windBlowR(range_)

if __name__ == '__main__':
    change = 'l'
    b = Bass(change)
    t1 = threading.Thread(target=b.KeyboardListener, args=())
    t1.start()
    while True:
        b.windBlow()

# while True:
# ...     time.sleep(.2)
# ...     print(('a '*42) if count%2==0 else (' a'*42))
# ...     count+=1
