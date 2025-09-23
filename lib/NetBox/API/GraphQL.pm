package NetBox::API::GraphQL;
use strict;
use warnings 'FATAL' => 'all';
no warnings qw(experimental::signatures);
use feature qw(signatures);
use parent qw(NetBox::API::Common);

use Data::Dumper;
use GraphQL::Client;

BEGIN {
    #{{{
    require Exporter;
    our @ISA = qw(Exporter);
    our @EXPORT = qw();
    our @EXPORT_OK = qw();
} #}}}

our $VERSION = $NetBox::API::Common::VERSION;

sub __call :prototype($$$$$) ($class, $self, $method, $query, $vars = {}) {
    #{{{
    return $class->GET($self, $query, $vars) if $method eq 'GET';
    $self->__seterror(NetBox::API::Common::E_NOMETHOD, $class, $method);
    return !$self->error;
} #}}}

sub GET :prototype($$$$) ($class, $self, $query, $vars = {}) {
    #{{{
    my $graphql = GraphQL::Client->new('url' => $self->baseurl, 'unpack' => 0);
    my $headers = $self->headers;
    my $fields = join ', ', @{$vars->{'fields'}};
    delete $vars->{'fields'};
    my $q = sprintf 'query %s ($id: ID!) { %s(id: $id) { %s } }', $query, $query, $fields;
    my $response = $graphql->execute($q, $vars, $query, { 'headers' => $headers });
    return defined $response->{'data'}{$query} ? ( $response->{'data'}{$query} ) : qw();
} #}}}

1;
