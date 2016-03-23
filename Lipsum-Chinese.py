# This Source Code Form is subject to the terms of the BSD Public

import sublime, sublime_plugin

class AbitCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(), "锄禾日当午~")

class SomeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(), "韶华不为少年留，恨悠悠，几时休。")

class LotsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(), "北京下大雨，大街上水很深。很多车都过不去。一打伞的哥们站在没过膝盖的水中。这时一开路虎越野车的大哥用藐视的目光看了看旁边的车，加大油门冲了过去，结果整车全部淹的都看不见了。车主好不容易从车里爬上来对打伞的哥们说：“水不是才到你膝盖吗？”打伞的哥们回到：“爷我站车顶上呢！”")

class StickCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(), "斑驳的旧时光里，总有一些或深或浅温暖人心的馨香，让人舍不得遗忘。潮湿的过往，不经意间邂逅了谁的眼眸；文字里泛舟，又与谁的倩影不期而遇？淡淡的墨香中，谁在翩然靠近，袅袅娜娜，直抵心间？一切，都那么美，那么惆怅，这不仅仅是文字的描摹，其外还有收藏着的心思与情感。的确，光阴里曾经明媚或暗淡的过往，总是伴着美丽的忧伤与成长的阵痛；日渐淡薄的往昔，也总能或多或少的在心里留下一丝清雅的执念。收藏，是因为骨子里是个守旧的人；收藏，更是因为心里有值得铭记的感动。今生，心为笔，写下满笺素心浅事，不求浮华，但求安然；今生，心作尘，用绵长的时光，写下一份浅淡，缓缓落墨，轻轻收笔。")

