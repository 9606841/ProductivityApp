class Daily:

  def __init__(self, title, freq):
    self.title = title
    self.freq = freq
  
  def makeDaily(self):
    self.title = input('What is your daily called?')
    self.freq = input('How often do you want to do this daily?')