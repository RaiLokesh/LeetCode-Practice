class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.ptr = 1
    def visit(self, url: str) -> None:
        for i in range(len(self.stack)-self.ptr):
            self.stack.pop()
        self.stack.append(url)
        self.ptr = len(self.stack)
    def back(self, steps: int) -> str:
        self.ptr -= min(self.ptr, steps)
        if self.ptr == 0:
            self.ptr += 1
        return self.stack[self.ptr-1]

    def forward(self, steps: int) -> str:
        self.ptr += min(len(self.stack)-self.ptr, steps)
        return self.stack[self.ptr-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)