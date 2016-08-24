import random

text = open('aesw2016(v1.2)_train.xml')
original_file = open('src-train.txt', 'w')
edited_file = open('targ-train.txt', 'w')

line = text.readline()

selection_p = 200000/722742.
corrected_sentences = 0
selected_right_sentences = 0

while line:

    if (line.find("<sentence")) > 0:

        start = line.find(">")
        finish = line.find("</sentence>")
        line = line[(start+1):finish]

        original = line
        edited = line

        if (line.count("<ins>")+line.count("<del>")) > 0:

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

            corrected_sentences += 1

            print line
            print original
            print edited

            original_file.write(original+'\n')
            edited_file.write(edited+'\n')

        else:
            if random.random() < selection_p:

                print line
                print original
                print edited

                original_file.write(original+'\n')
                edited_file.write(edited+'\n')

                selected_right_sentences += 1

    line = text.readline()

print "Number of selected right sentences = ", selected_right_sentences
print "Number of selected edited sentences = ", corrected_sentences
text.close()
original_file.close()
edited_file.close()
