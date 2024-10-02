"""
Treat all arguments passed by the user.
"""

def treat_args(data, organism: str, product: str, biosynt: str,
               completeness: str, minimal: bool) -> bool:
    '''
    Lower all user inputs an compare to lowered metadata. Evaluate the
    presence of an argument and include it in treatment

    Arguments:
    organism -- target organism name
    product -- target compound name
    biosynt -- target biosynthetic class name
    completeness -- Cluster completeness from mibig
    mininal -- annotation status from mibig
    '''

    add: bool = True

    if organism:
        add &= organism.lower() in data['cluster']['organism_name'].lower()
    if product:
        add &= product.lower() in [
            c.get('compound').lower() for c in data['cluster']['compounds']
            ]
    if biosynt:
        add &= biosynt.lower() in [
            b.lower() for b in data['cluster']['biosyn_class']
            ]

    add &= (
        data['cluster']['loci']['completeness'].lower() == completeness.lower()
        )
    add &= data['cluster']['minimal'] is minimal

    return add
