use ExtUtils::MakeMaker;

WriteMakefile(
    dist	 => {},
    NAME         => "NetBox::API",
    VERSION_FROM => "lib/NetBox/API/Common.pm",
    clean        => {},
);

