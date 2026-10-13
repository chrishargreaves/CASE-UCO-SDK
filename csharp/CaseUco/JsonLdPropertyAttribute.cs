using System;

namespace CaseUco
{
    [AttributeUsage(AttributeTargets.Property, AllowMultiple = false, Inherited = true)]
    public sealed class JsonLdPropertyAttribute : Attribute
    {
        public JsonLdPropertyAttribute(string key)
        {
            Key = key;
        }

        public string Key { get; }

        /// <summary>XSD datatype for ranges the CLR type does not determine (byte[] as xsd:hexBinary or xsd:base64Binary).</summary>
        public string Datatype { get; set; }
    }
}
