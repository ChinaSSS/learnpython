#系统客户端
import win32com.client

man = win32com.client.Dispatch("SAPI.SPVOICE")
man.Speak("i am ironman")