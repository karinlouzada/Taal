import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        add(name)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")

    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )


def add(name):
    # read in existing data
    file1 = open('sample.dat', 'r')
    Lines = file1.readlines()
    file1.close()
    # reopen file to enter data
    file2 = open('sample.dat', 'w')

    count = 0
    # insert new datum into list
    Lines.insert(1, '"'+name.upper()+'",\n')
    # create set to remove doubles
    Lines_temp = set(Lines[1:len(Lines)-1])
    # recreate list and sort
    Lines = list(Lines_temp)
    Lines.sort()

    # write data to file including headers and footers.
    file2.writelines('let WORDS = [\n')
    for line in Lines:
        count += 1
        file2.writelines(line)
    file2.writelines('];\n')
    file2.close()
