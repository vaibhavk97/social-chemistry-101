"""Module that can be edited and reloaded to live supply a generation script with
material.

The purpose of this is to make it easy to see how the model changes its generations when
an attribute is varied.

Used by sc/examples/generate.py. You probably want to run that.
"""

import code
import typing
from typing import List, Tuple, Set, Dict, Any, Optional, NamedTuple, Iterator

MFS = (
    "Moral Foundations",
    [
        "care-harm",
        "fairness-cheating",
        "loyalty-betrayal",
        "authority-subversion",
        "sanctity-degradation",
    ],
)

CATS = (
    "Rule-of-Thumb Category",
    [
        "morality-ethics",
        "social-norms",
        # "advice",  # rarely want these
        # "description",  # off by default, as very rarely want these
    ],
)

AGREEMENTS = (
    "How many people probably agree with this ROT?",
    [
        # People basically didn't write ROTs for these categories. (Which is expected.)
        # "nobody",
        # "rare",
        "controversial",
        "most",
        "all",
    ],
)

PRESSURES = (
    "How much cultural pressure do you feel to do the action?",
    ["strong-against", "against", "discretionary", "for", "strong-for"],
)

MORAL_JUDGMENTS = (
    "How good/bad is it to do the action morally?",
    ["very-bad", "bad", "ok", "good", "very-good"],
)

LEGAL = ("Is the action legal?", ["illegal", "tolerated", "legal"])


Examples = List[Tuple[str, Tuple[str, List[str]]]]


def action_agreement() -> Examples:
    return [
        (
            "Calling the police on my neighbors. [attrs] <agency> <ok> <{varies}> <legal> [action]",
            AGREEMENTS,
        )
    ]


def action_pressure() -> Examples:
    # also varying moral judgment
    return [
        (
            "Calling the police on my neighbors. [attrs] <agency> <bad> <most> <legal> <{varies}> <hypothetical> [action]",
            PRESSURES,
        )
    ]

def action_legal() -> Examples:
    return [
        (
            "Calling the police on my neighbors. [attrs] <agency> <good> <most> <{varies}> <for> <hypothetical> [action]",
            LEGAL,
        )
    ]

def action_custom() -> Examples:
    return [
        (
            "Wanting to stay out after curfew. [attrs] <agency> <good> <most> <{varies}> <for> <hypothetical> [action]",
            LEGAL,
        )
    ]

def action_examples() -> Examples:
    """This function is called by sc/examples/generate.py to get action inputs."""
    # return action_agreement()
    # return action_pressure()
    # return action_legal()
    return action_custom()


def rot_examples() -> Examples:
    """This function is called by sc/examples/generate.py to get RoT inputs."""
    import json

    with open('../dialogue/train.json') as ofile:
        data = json.load(ofile)

    context_set = set()

    for x in data:
        context_set.add(data[x]['context'])
    final_list = list()
    for x in context_set:
        final_list.append((x+" [attrs] <{varies}> <all> [rot]", CATS),)
    return final_list
