# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,380 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.ICONIZE|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Set_Tx_Carrier_Frequency_ARM" ), wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Carrier_Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer3.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		carrier_control_comboboxChoices = [ u"0x00 - Carrier On", u"0x01 - Carrier Off" ]
		self.carrier_control_combobox = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, carrier_control_comboboxChoices, 0 )
		self.carrier_control_combobox.SetSelection( 0 )
		bSizer3.Add( self.carrier_control_combobox, 1, wx.ALL, 5 )


		sbSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Carrier_Frequency (encoded)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer31.Add( self.m_staticText11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.carrier_frequency_textbox = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"2402", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.carrier_frequency_textbox, 1, wx.ALL, 5 )


		sbSizer1.Add( bSizer31, 0, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Modulation_Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer32.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		modulation_comboboxChoices = [ u"0x00 - Un-modulated", u"0x01 - PRBS9 sequence", u"0x02 - PRBS15 sequence", u"0x03 - repeated '00000000'", u"0x04 - repeated '11111111'", u"0x05 - incrementing symbols" ]
		self.modulation_combobox = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, modulation_comboboxChoices, 0 )
		self.modulation_combobox.SetSelection( 0 )
		bSizer32.Add( self.modulation_combobox, 1, wx.ALL, 5 )


		sbSizer1.Add( bSizer32, 0, wx.EXPAND, 5 )

		bSizer321 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText121 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Modulation_Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		bSizer321.Add( self.m_staticText121, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		modulation_type_comboboxChoices = [ u"0x00 - GFSK (1Mb/s)", u"0x01 - QPSK (2Mb/s)", u"0x02 - 8DPSK (3Mb/s)" ]
		self.modulation_type_combobox = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, modulation_type_comboboxChoices, 0 )
		self.modulation_type_combobox.SetSelection( 0 )
		bSizer321.Add( self.modulation_type_combobox, 1, wx.ALL, 5 )


		sbSizer1.Add( bSizer321, 0, wx.EXPAND, 5 )

		bSizer3211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1211 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Transmit_Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1211.Wrap( -1 )

		bSizer3211.Add( self.m_staticText1211, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		transmitt_power_comboboxChoices = [ u"0x00 - 0 dBm", u"0x01 - -4 dBm", u"0x02 - -8dBm", u"0x03 - -12 dBm", u"0x04 - -16 dBm", u"0x05 - -20 dBm", u"0x06 - -24 dBm", u"0x07 - -28dBm", u"0x08 - Specify power in dBm", u"0x09 - Specify power table index" ]
		self.transmitt_power_combobox = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, transmitt_power_comboboxChoices, 0 )
		self.transmitt_power_combobox.SetSelection( 0 )
		bSizer3211.Add( self.transmitt_power_combobox, 1, wx.ALL, 5 )


		sbSizer1.Add( bSizer3211, 0, wx.EXPAND, 5 )

		bSizer32111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12111 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Transmit_Power_dBm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12111.Wrap( -1 )

		bSizer32111.Add( self.m_staticText12111, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.transmitt_power_dbm_textbox = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0x00", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32111.Add( self.transmitt_power_dbm_textbox, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer1.Add( bSizer32111, 0, wx.EXPAND, 5 )

		bSizer321111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText121111 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Transmit_Power_Table_Index", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121111.Wrap( -1 )

		bSizer321111.Add( self.m_staticText121111, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.transmitt_power_table_index_textbox = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, u"0x00", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer321111.Add( self.transmitt_power_table_index_textbox, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer1.Add( bSizer321111, 0, wx.EXPAND, 5 )

		self.carrier_off_command = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Copy Carrier Off Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.carrier_off_command, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Command Generation" ), wx.VERTICAL )

		bSizer3211111 = wx.BoxSizer( wx.HORIZONTAL )

		self.command_textbox = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer3211111.Add( self.command_textbox, 1, wx.ALL|wx.EXPAND, 5 )

		self.Copy_Command = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Copy Command", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3211111.Add( self.Copy_Command, 0, wx.ALL, 5 )


		sbSizer2.Add( bSizer3211111, 1, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer2, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.carrier_control_combobox.Bind( wx.EVT_COMBOBOX, self.carrier_control_comboboxOnCombobox )
		self.carrier_frequency_textbox.Bind( wx.EVT_TEXT, self.carrier_frequency_textboxOnText )
		self.modulation_combobox.Bind( wx.EVT_COMBOBOX, self.modulation_comboboxOnCombobox )
		self.modulation_type_combobox.Bind( wx.EVT_COMBOBOX, self.modulation_type_comboboxOnCombobox )
		self.transmitt_power_combobox.Bind( wx.EVT_COMBOBOX, self.transmitt_power_comboboxOnCombobox )
		self.transmitt_power_dbm_textbox.Bind( wx.EVT_TEXT, self.transmitt_power_dbm_textboxOnText )
		self.transmitt_power_table_index_textbox.Bind( wx.EVT_TEXT, self.transmitt_power_table_index_textboxOnText )
		self.carrier_off_command.Bind( wx.EVT_BUTTON, self.carrier_off_commandOnButtonClick )
		self.Copy_Command.Bind( wx.EVT_BUTTON, self.Copy_CommandOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def carrier_control_comboboxOnCombobox( self, event ):
		event.Skip()

	def carrier_frequency_textboxOnText( self, event ):
		event.Skip()

	def modulation_comboboxOnCombobox( self, event ):
		event.Skip()

	def modulation_type_comboboxOnCombobox( self, event ):
		event.Skip()

	def transmitt_power_comboboxOnCombobox( self, event ):
		event.Skip()

	def transmitt_power_dbm_textboxOnText( self, event ):
		event.Skip()

	def transmitt_power_table_index_textboxOnText( self, event ):
		event.Skip()

	def carrier_off_commandOnButtonClick( self, event ):
		event.Skip()

	def Copy_CommandOnButtonClick( self, event ):
		event.Skip()


