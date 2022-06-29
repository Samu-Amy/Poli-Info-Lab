# button_frame = Frame(self._main, background=self._back_color)
# button = Button(button_frame, image=image, width=60, height=50, borderwidth=0)
# label = ttk.Label(button_frame, text=name)
#
# self.change_on_hover_multiples(button_frame, self._light_blue, self._back_color, button_frame, button, label)
#
# button_frame.bind("<Button-1>", lambda event: self._controller.open(index))
# button.bind("<Button-1>", lambda event: self._controller.open(index))
# label.bind("<Button-1>", lambda event: self._controller.open(index))
#
# button_frame.bind("<Button-3>", lambda event: self.do_popup(index))  #TODO: da sistemare
#
# button_frame.grid(row=self._rows, column=col, padx=8, pady=8, sticky="nw")
# button.grid(row=0, column=0, sticky="s")
# label.grid(row=1, column=0, sticky="n")
#
# self._buttons.append(button_frame)