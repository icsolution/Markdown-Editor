class MarkdownEditor:

    def __init__(self):
        self.result = ''
        self.prompt()

    def prompt(self):
        choice = input('Choose a formatter: ')
        self.formatter(choice)

    def formatter(self, choice):
        options = 'plain bold italic header link inline-code ordered-list unordered-list new-line line-break'
        if choice in options:
            if 'list' in choice:
                self.list(choice)
                self.new_line()
            else:
                exec(f"self.{choice.replace('-','_')}()")
            print(self.result)
            self.prompt()
        elif choice == '!help':
            print('Available formatters: plain bold italic header link inline-code new-line')
            print('Special commands: !help !done')
            self.prompt()
        elif choice == '!done':
            with open('output.md', 'w') as file:
                file.write(self.result)
            exit()
        else:
            print('Unknown formatting type or command')
            self.prompt()

    @staticmethod
    def text():
        return input('Text: ')

    def plain(self):
        self.result += self.text()

    def bold(self):
        self.result += f'**{self.text()}**'

    def italic(self):
        self.result += f'*{self.text()}*'

    def header(self):
        level = int(input('Level: '))
        if 1 <= level <= 6:
            self.result += level * r'#' + f' {self.text()}\n'
        else:
            print('The level should be within the range of 1 to 6')
            self.header()

    def link(self):
        label = input('Label: ')
        url = input('URL: ')
        self.result += f'[{label}]({url})'

    def inline_code(self):
        self.result += f'`{self.text()}`'

    def new_line(self):
        self.result += '\n'

    def list(self, choice):
        formatted_list = []
        rows = int(input('Number of rows: '))
        if rows <= 0:
            print('The number of rows should be greater than zero')
            self.list(choice)
        elements = [input(f'Row #{row + 1}: ') for row in range(rows)]
        for index, text in enumerate(elements):
            if 'unordered' in choice:
                formatted_list.append(f'* {text}')
            else:
                formatted_list.append(f'{index + 1}. {text}')
        self.result += '\n'.join(formatted_list)

    def line_break(self):
        print(self.result + '\n')
        self.prompt()


MarkdownEditor()
