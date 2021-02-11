from chatterbot.logic import LogicAdapter
from nltk.sentiment import SentimentIntensityAnalyzer

from sugaroid.core.statement import SugaroidStatement


class SugaroidLogicAdapter(LogicAdapter):
    """
    This is an abstract class that represents the interface
    that all logic adapters should implement.

    :param search_algorithm_name: The name of the search algorithm that should
        be used to search for close matches to the provided input.
        Defaults to the value of ``Search.name``.

    :param maximum_similarity_threshold:
        The maximum amount of similarity between two statement that is required
        before the search process is halted. The search for a matching statement
        will continue until a statement with a greater than or equal similarity
        is found or the search set is exhausted.
        Defaults to 0.95

    :param response_selection_method:
          The a response selection method.
          Defaults to ``get_first_response``
    :type response_selection_method: collections.abc.Callable

    :param default_response:
          The default response returned by this logic adaper
          if there is no other possible response to return.
    :type default_response: str or list or tuple
    """

    def __init__(self, chatbot, **kwargs):
        super(SugaroidLogicAdapter, self).__init__(chatbot, **kwargs)
        self.sia = SentimentIntensityAnalyzer()

    def can_process(self, statement: SugaroidStatement) -> bool:
        """
        Checks if Sugaroid can process a statement
        :param statement: The statement to do prelimnary checks
        :type statement: SugaroidStatement
        :return: True, if the statement be processed, else False
        :rtype: bool
        """
        return super(SugaroidLogicAdapter, self).can_process(statement)

    def Tprocess(
        self,
        statement: SugaroidStatement,
        additional_response_selection_parameters=None,
    ) -> SugaroidStatement:
        """
        Processes the statement in detail
        :param statement: The statement from the user to process
        :type statement: SugaroidStatement
        :param additional_response_selection_parameters:
        :type additional_response_selection_parameters:
        :return: The Statement from the logic adapter once its processed
        :rtype: SugaroidStatement
        """
        response = super(SugaroidLogicAdapter, self).process(
            statement, additional_response_selection_parameters
        )
        response = SugaroidStatement.from_statement(response)
        response.set_chatbot(True)
        return response
