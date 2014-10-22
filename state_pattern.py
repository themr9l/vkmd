
class Machine:
    def __init__(self):
        print('create Machine')
        pass

    def set_current_state(self, state):
        print('set current state {0}'.format(state))
        self.current_state = state

    def on(self):
        self.current_state.on(self)
        pass

    def off(self):
        self.current_state.off(self)
        pass
        
class State:
    def __init__(self):
        pass

    def on(self, machine):
        new_state = ON()
        print('from state {0} to state {1}'.format(machine.current_state, new_state))
        machine.set_current_state(new_state)

    def off(self, machine):
        new_state = OFF()
        print('from state {0} to state {1}'.format(machine.current_state, new_state))
        machine.set_current_state(new_state)

class ON(State):
    def __init__(self):
        pass

class OFF(State):
    def __init__(self):
        pass

print('LOLOOKSDFFFF')
m = Machine()
m.set_current_state(ON())
m.off()