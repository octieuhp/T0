import os
import time

def Test_Ping2_5G(parent, dut_id, ip, inteface='', log):
    '''
    Function test ping 2.5G ethernet card

    '''
    start_time = time.time()
    parent.SendMessage(dut_id, "Test ping 2.5G ethernet card start....\n", log)
    if not inteface:
        result = os.popen("ping %s"%ip).read()
    else:
        result = os.popen("ping %s -S %s"%(ip, inteface)).read()
    if "Lost = 0 (0% loss)" in data:
        parent.SendMessage(dut_id, "Test ping 2.5G ethernet pass\n", log)
    else:
        raise Except("Test ping 2.5G ethernet fail", log)
    parent.SendMessage("Test time: %s"%(time.time() - start_time), log)
    parent.SendMessage(dut_id,"---------------------------------------------------------------------------\n",log)

def BBU_UART_COMMUNICATION(parent, dut_id, term, log):
    '''
        Function test Battery uart communication
    '''
    start_time = time.time()
    parent.SendMessage(dut_id, "Battery test Start...\n", log)
    #com_port = comport[dut_id]
    term_uart = htx.SerialTTY(comport[dut_id], int(b_rate))     # baurate = b_rate = 9600
    #start_time = time.time()
    lWaitCmdTerm(term, "shell", '#', 8, 2)

    for i in range(5):
        lWaitCmdTerm(term, "battery_host -m 3 -v", '#', 8, 2)
        result = term_uart.wait("\xd4", 5)[-1]
        print result
        if "\xaa\x05\xe0\xcf\x00v\xd4" in data:
            parent.SendMessage(dut_id, "Check Battery connect pass.\n", log)
            break
        elif i == 4: raise Except("Battery connect fail.")
    
    for i in range(5):
        term << "battery_host -m 3 -v"
        time.sleep(0.5)
        term_uart << "\xaa \x03 \x06 \x4f \xc8"
        result = term.wait("aa 20 03 20 06 20 4f 20 c8 0d", 8)[-1]
        print result
        if "aa 20 03 20 06 20 4f 20 c8 0d" in data:
            parent.SendMessage(dut_id, "Battery test pass.\n", log)
            break
        elif i == 4: raise Except("Battery test fail")
    lWaitCmdTerm(term, "exit", "nu>", 8)
    parent.SendMessage(dut_id, "Battery test time: %d\n"%(time.time() - start_time), log)
    parent.SendMessage(dut_id,"---------------------------------------------------------------------------\n",log)


