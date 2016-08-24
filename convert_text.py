# text = open('aesw2016(v1.2)_dev.xml')
# original_file = open('src-val.txt', 'w')
# edited_file = open('targ-val.txt', 'w')

text = open('test.evaluation.xml')
original_file = open('src-test.txt', 'w')
edited_file = open('targ-test.txt', 'w')

line = text.readline()

while line:

    if (line.find("<sentence sid")) > 0:

        start = line.find(">")
        finish = line.find("</sentence>")
        line = line[(start+1):finish]

        original = line
        edited = line

        for x in xrange(0, line.count("<ins>")):

            start = original.find("<ins>")
            finish = original.find("</ins>")
            original = original[:start] + original[(finish+6):]

            start = edited.find("<ins>")
            finish = edited.find("</ins>")
            edited = edited[:start] + edited[(start+5):finish] + edited[(finish+6):]

        for x in xrange(0, line.count("<del>")):

            start = edited.find("<del>")
            finish = edited.find("</del>")
            edited = edited[:start] + edited[(finish+6):]

            start = original.find("<del>")
            finish = original.find("</del>")
            original = original[:start] + original[(start+5):finish] + original[(finish+6):]

        print line
        print original
        print edited

        original_file.write(original+'\n')
        edited_file.write(edited+'\n')

    line = text.readline()

text.close()
original_file.close()
edited_file.close()

