"""
MIT License

Copyright (c) 2021 Benjamin Ramberg Møklegård (benrammok)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import wx
import gui_wx
from wx import Clipboard

class GUI(gui_wx.MyFrame1):
    def __init__(self, parent):
        gui_wx.MyFrame1.__init__(self, parent)
        self.command_text_default = "hcitool -i hci0 cmd 0x3F 0x14 P1 P2 P3 P4 P5 P6 P7"
        self.command_text = ""
        self.carrier_frequency = ""
        self.dbm_power = "0x00"
        self.dbm_index = "0x00"
        self.carrier_frequency_textboxOnText(event=None)

    def generate_hci_command(self):
        self.command_text = self.command_text_default
        carrier_enable = self.carrier_control_combobox.GetValue().split(' - ')[0]
        carrier_frequency = "0x00" if self.carrier_frequency == "" else self.carrier_frequency
        modulation_mode = self.modulation_combobox.GetValue().split(' - ')[0]
        mod_type = '0x00' if modulation_mode == '0x00' else self.modulation_type_combobox.GetValue().split(' - ')[0]
        transmit_power = self.transmitt_power_combobox.GetValue().split(' - ')[0]
        transmit_power_dbm = '0x00' if transmit_power != '0x08' \
            else self.dbm_power
        transmit_power_table_index = '0x00' if transmit_power != '0x09' \
            else self.dbm_index

        if carrier_enable == '0x01':
                self.command_text = self.command_text_default.split('P2')[0].strip(' ')
                self.command_text = self.command_text.replace('P1', carrier_enable)
                print(self.command_text)
        else:
            self.command_text = self.command_text.replace('P1', carrier_enable)
            self.command_text = self.command_text.replace('P2', carrier_frequency)
            self.command_text = self.command_text.replace('P3', modulation_mode)
            self.command_text = self.command_text.replace('P4', mod_type)
            self.command_text = self.command_text.replace('P5', transmit_power)
            self.command_text = self.command_text.replace('P6', transmit_power_dbm)
            self.command_text = self.command_text.replace('P7', transmit_power_table_index)

        self.command_textbox.Value = self.command_text



    def carrier_control_comboboxOnCombobox(self, event):
        command_value = self.carrier_control_combobox.GetValue().split('-')[0].strip(' ')
        if command_value == '0x01':
            self.carrier_frequency_textbox.Enable(False)
            self.modulation_combobox.Enable(False)
            self.modulation_type_combobox.Enable(False)
            self.transmitt_power_combobox.Enable(False)
            self.transmitt_power_dbm_textbox.Enable(False)
            self.transmitt_power_table_index_textbox.Enable(False)
        else:
            self.carrier_frequency_textbox.Enable(True)
            self.modulation_combobox.Enable(True)
            self.modulation_type_combobox.Enable(True)
            self.transmitt_power_combobox.Enable(True)
            self.transmitt_power_dbm_textbox.Enable(True)
            self.transmitt_power_table_index_textbox.Enable(True)
        self.generate_hci_command()

    def carrier_frequency_textboxOnText(self, event):
        carrier_frequency_text = self.carrier_frequency_textbox.GetValue()
        if carrier_frequency_text.isdigit():
            carrier_frequency_num = int(carrier_frequency_text)
            if 2402 <= carrier_frequency_num <= 2480:
                self.carrier_frequency = "0x{:02X}".format(carrier_frequency_num - 2400)
                self.generate_hci_command()

    def modulation_comboboxOnCombobox(self, event):
        self.generate_hci_command()

    def modulation_type_comboboxOnCombobox(self, event):
        self.generate_hci_command()

    def transmitt_power_comboboxOnCombobox(self, event):
        self.generate_hci_command()

    def transmitt_power_dbm_textboxOnText(self, event):
        dBm = self.transmitt_power_dbm_textbox.GetValue()
        if dBm.isdigit():
            dBm_digit = int(dBm)
            print(int('0xFF', 16))
            if int('0x00', 16) <= dBm_digit <= int('0xFF', 16):
                self.dbm_power = "0x{:02X}".format(dBm_digit)
                print("Generate")
                self.generate_hci_command()

    def transmitt_power_table_index_textboxOnText(self, event):
        index = self.transmitt_power_dbm_textbox.GetValue()
        if index.isdigit():
            index_digit = int(index)
            if int('0x00', 16) <= index_digit <= int('0xFF', 16):
                self.dbm_index = "0x{:02X}".format(index_digit)
                self.generate_hci_command()

    def carrier_off_commandOnButtonClick(self, event):
        self.generate_hci_command()

    def Copy_CommandOnButtonClick( self, event ):
        if Clipboard.Open():
            Clipboard.Clear()
            Clipboard.SetData(wx.TextDataObject(self.command_textbox.GetValue()))

app = wx.App(False)
gui = GUI(parent=None)
gui.Show(True)
app.MainLoop()
