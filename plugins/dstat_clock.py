### Dstat clock plugin
### Displays human readable clock
###
### Authority: dag@wieers.com

class dstat_clock(dstat):
	def __init__(self):
		self.name = 'clock'
		self.format = ('s', 14, 0)
		self.nick = ('date/time',)
		self.vars = self.nick

	def extract(self):
		pass

	def show(self):
		return time.strftime('%d-%m %H:%M:%S', time.localtime())

# vim:ts=4:sw=4
