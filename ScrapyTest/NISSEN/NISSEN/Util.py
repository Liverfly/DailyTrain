def ex_element_css(s, d, leaf=True, *pths):
    '''
    extract element.
    s -- selector
    d -- default value
    pths -- css paths
    @return: `d` if not found.
    '''
    return _ex_element(s, d, 'css', leaf, *pths)

def ex_element_xpath(s, d, leaf=True, *pths):
    '''
    extract element.
    s -- selector
    d -- default value
    pths -- xpath paths
    @return: `d` if not found.
    '''
    return _ex_element(s, d, 'xpath', leaf, *pths)

def _ex_element(s, d='', m='xpath', leaf=True, *pths):
    '''
    extract element.
    s -- selector
    d -- default value
    m -- method, ['xpath', 'css']
    pths -- xpath 's or css 's
    @return: `d` if not found.
    '''
    r = d
    for p in pths:
        r_ = getattr(s, m)(p)
        if not r_:
            continue
        elif leaf:
            r = r_.extract()
        else:
            r = r_
        break
    return r