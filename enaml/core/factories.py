#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
class ReadScopeFactory(object):
    """ A base class for definining read scope factories.

    A read scope factory is used to create scope objects for executing
    a bound expression which provides a value.

    """
    __slots__ = ()

    def __call__(self, owner, storage):
        """ Create and return a scope object for reading an expression.

        This method must be implemented by subclasses.

        Parameters
        ----------
        owner : Declarative
            The declarative object which is reading an exression.

        storage : sortedmap
            The shared storage map for the declarative object.

        Returns
        -------
        result : mapping
            A mapping object which implements the scope.

        """
        raise NotImplementedError


class WriteScopeFactory(object):
    """ A base class for definining write scope factories.

    A write scope factory is used to create scope objects for executing
    a bound expression which depends upon the context change.

    """
    __slots__ = ()

    def __call__(self, owner, storage, change):
        """ Create and return a scope object for writing an expression.

        This method must be implemented by subclasses.

        Parameters
        ----------
        owner : Declarative
            The declarative object which is reading an exression.

        storage : sortedmap
            The shared storage map for the declarative object.

        change : dict
            The change dictionary generated by the declarative object.

        Returns
        -------
        result : mapping
            A mapping object which implements the scope.

        """
        raise NotImplementedError


class TracedReadScopeFactory(object):
    """ A base class for definining traced read scope factories.

    A traced read scope factory is used to create scope objects for
    excecuting a bound expression with tracing.

    """
    __slots__ = ()

    def __call__(self, owner, storage, tracer):
        """ Create a return a scope object for reading an expression.

        This method must be implemented by subclasses.

        Parameters
        ----------
        owner : Declarative
            The declarative object which is reading an exression.

        storage : sortedmap
            The shared storage map for the declarative object.

        tracer : CodeTracer
            A code tracer which should be notified on a dynamic
            attribute load.

        Returns
        -------
        result : mapping
            A mapping object which implements the scope.

        """
        raise NotImplementedError


class CodeTracerFactory(object):
    """ A base class for defining code tracer factories.

    A code tracer factory is used to create a code tracer for tracing
    the execution of a bound expression.

    """
    __slots__ = ()

    def __call__(self, owner, name, storage):
        """ Create and return a code tracer.

        This method must be implemented by subclasses.

        Parameters
        ----------
        owner : Declarative
            The declarative object which is reading an exression.

        name : str
            The name of the attribute on the owner for which the
            expression is being evaluated.

        storage : sortedmap
            The shared storage map for the declarative object.

        Returns
        -------
        result : CodeTracer
            A code tracer object which will perform the tracing.

        """
        raise NotImplementedError


class CodeInverterFactory(object):
    """ A base class for defining code inverter factories.

    A code inverter factory is used to create a code inverter for
    inverting the execution of a bound expression.

    """
    __slots__ = ()

    def __call__(self, owner, name, storage):
        """ Create and return a code inverter.

        This method must be implemented by subclasses.

        Parameters
        ----------
        owner : Declarative
            The declarative object which is writing an exression.

        name : str
            The name of the attribute on the owner for which the
            expression is being written.

        storage : sortedmap
            The shared storage map for the declarative object.

        Returns
        -------
        result : CodeInverter
            A code inverter object which will perform the inversion.

        """
        raise NotImplementedError
