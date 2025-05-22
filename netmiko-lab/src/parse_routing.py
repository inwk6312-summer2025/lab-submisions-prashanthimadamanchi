import textfsm

def parse_routing_table(output):
    with open("cisco_routing_table.textfsm") as fsm_template:
        fsm = textfsm.TextFSM(fsm_template)
        results = fsm.ParseText(output)
        return [dict(zip(fsm.header, row)) for row in results]

# Example usage:
if __name__ == "__main__":
    with open("R1_routing_output.txt") as f:
        output = f.read()
    parsed = parse_routing_table(output)
    for entry in parsed:
        print(entry)


