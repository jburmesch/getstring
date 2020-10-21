from sys import exit


def get_string(prompt: str, max_words=0, min_words=1, max_chars=0, min_chars=1,
               options=[], case_sensitive_options=False, proper_case=False,
               confirm_retry=False):
    answer = input(prompt + "\n")

    if proper_case:
        answer = answer.title()

    if max_words != 0:
        if len(answer.split()) > max_words:
            print(f'Error: No more than {max_words} word(s) may be entered.')
            return retry(prompt, max_words, min_words, max_chars, min_chars,
                         options, case_sensitive_options, proper_case,
                         confirm_retry)

    if len(answer.split()) < min_words:
        print(f'Error: At least {min_words} word(s) must be entered.')
        return retry(prompt, max_words, min_words, max_chars, min_chars,
                     options, case_sensitive_options, proper_case,
                     confirm_retry)

    if max_chars > 0:
        if len(answer) > max_chars:
            print(f'Error: No more than {max_chars} character(s) may be '
                  + 'entered.')
            return retry(prompt, max_words, min_words, max_chars, min_chars,
                         options, case_sensitive_options, proper_case,
                         confirm_retry)

    if len(answer) < min_chars:
        print(f'Error: At least {min_chars} character(s) must be entered.')
        return retry(prompt, max_words, min_words, max_chars, min_chars,
                     options, case_sensitive_options, proper_case,
                     confirm_retry)

    if len(options) > 0:
        if case_sensitive_options:
            if answer not in options:
                print(f'Error: Input options are: {options}. '
                      + '\n Options are case-sensitive.')
                return retry(prompt, max_words, min_words, max_chars,
                             min_chars, options, case_sensitive_options,
                             proper_case, confirm_retry)
        else:
            upper_options = []
            for option in options:
                upper_options.append(option.upper())
            if answer.upper() not in upper_options:
                print(f'Error: Input options are: {options} '
                      + '\n Options are not case-sensitive.')
                return retry(prompt, max_words, min_words, max_chars,
                             min_chars, options, case_sensitive_options,
                             proper_case, confirm_retry)

    return answer


def retry(prompt, max_words, min_words, max_chars, min_chars, options,
          case_sensitive_options, proper_case, confirm_retry):
    if confirm_retry:
        answer = ""
        while answer.upper() != 'Y' and answer.upper() != 'N':
            answer = input('Retry? [Y/N]:')
        if answer.upper() == 'Y':
            return get_string(
                        prompt=prompt,
                        max_words=max_words,
                        min_words=min_words,
                        max_chars=max_chars,
                        min_chars=min_chars,
                        options=options,
                        case_sensitive_options=case_sensitive_options,
                        proper_case=proper_case,
                        confirm_retry=confirm_retry
                    )
        else:
            print('Exiting...')
            exit()
    else:
        return get_string(
                        prompt=prompt,
                        max_words=max_words,
                        min_words=min_words,
                        max_chars=max_chars,
                        min_chars=min_chars,
                        options=options,
                        case_sensitive_options=case_sensitive_options,
                        proper_case=proper_case,
                        confirm_retry=confirm_retry
                    )


if __name__ == "__main__":
    answer = get_string(
        'Please enter "This is a test."',
        options=['This is a test.'],
        case_sensitive_options=True
    )
    if answer == 'This is a test.':
        print("Success!")
