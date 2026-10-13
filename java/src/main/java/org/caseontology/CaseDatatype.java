package org.caseontology;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * Declares the XSD datatype of a generated field whose Java type does not
 * determine it, such as {@code byte[]} for {@code xsd:hexBinary} or
 * {@code xsd:base64Binary}.
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface CaseDatatype {
    String value();
}
